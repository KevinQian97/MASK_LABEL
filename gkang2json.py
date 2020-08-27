import json
import os
import argparse
from multiprocessing import Process
import re
from multiprocessing import Pool
import csv

def template(sf,ef,x1,y1,x2,y2):
    traj = {str(fid):[int(x1),int(y1),int(x2),int(y2)] for fid in range(int(sf),int(ef)+1) }
    res = {
        "end_frame":ef,
        "event_begin": sf,
        "event_end": ef,
        "event_type": "event_proposal",
        "par_offset_end": 1.0,
        "par_offset_st": 0.0,
        "parent": 0,
        "start_frame": sf,
        "trajectory":traj
    }
    return res

def file2nistapi(args):
    filename = args[0]
    out_dir = args[1]
    res = file2nist(filename,out_dir)
    return

def file2nist(filename,out_dir):
    print(filename)
    csvfile = open(filename,"r")
    reader = csv.reader(csvfile)
    res = {}
    for item in reader:
        if reader.line_num == 1:
            print(item)
            continue
        sf = int(item[4])
        ef = int(item[5])
        x1,y1,x2,y2 = item[6:]
        tid = item[1]
        prop = template(sf,ef,x1,y1,x2,y2)
        res[str(tid)] = prop
    csvfile.close()
    jname = os.path.join(out_dir,filename.split("/")[-1].strip(".csv")+".json")
    print(jname)
    # raise RuntimeError("sanity check")
    # jname = os.path.join(out_dir,os.path.basename(filename).strip('.txt').strip('.props') + '.json')
    with open(jname,'w') as j:
        json.dump(res,j,indent=2)
    j.close()
    return res

def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prop_dir', type=str, required=True, help='Path to location of list of videos')
    # parser.add_argument('--prop_lst', type=str,default='out.json', help='final json file in NIST format')
    parser.add_argument('--out_dir', type=str,default='props/', help='prop meta info dir')
    return parser.parse_args()

if __name__ == '__main__':
    config = parse_opts()
    jobs = []
    vids = os.listdir(config.prop_dir)
    if not os.path.exists(config.out_dir):
        os.makedirs(config.out_dir)
    args_list = []
    for vid in vids:
        pathi = os.path.join(config.prop_dir,vid)
        args_list.append([pathi,config.out_dir])
    
    n_jobs = 20
    pool = Pool(n_jobs)
    pool.map(file2nistapi, args_list)
    pool.close()

