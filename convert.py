import sys
import json
import subprocess
import zipfile
import glob
import shutil
import time

def toCoop(data): 
    return [{"data": {"coopHistoryDetail": json.loads(d)}} for d in data]

def toVersus(data):
    res = []
    for d in data:
        conv = json.loads(d)
        if "myTeam" in conv and "players" in conv["myTeam"]:
            res.append({"data": {"vsHistoryDetail": conv}}) 
    return res

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid call. Please use the following command:")
        print(sys.executable, sys.argv[0], "convert.py", "path/to/cblite_executable", "path/to/ikax3_file")
        exit()
    tool_name = sys.argv[1]
    assert "cblite" in tool_name
    filename = sys.argv[2]
    assert "ikax3" in filename
    shutil.rmtree("tmp", ignore_errors=True)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("tmp")
    dirs = glob.glob("tmp/*/*.cblite2")
    full_res = []
    for d in dirs:
        data_s = toCoop if "coopResult" in d else toVersus
        out = subprocess.check_output([tool_name, "cat", "--raw", d, "*"], encoding="utf8")
        full_res.extend(data_s(out.splitlines()))

    json.dump(full_res, open(f"converted_{int(time.time())}.json", "w"))