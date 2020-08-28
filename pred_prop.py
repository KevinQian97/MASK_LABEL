import csv
import json
import os

def make_blanket_output(labels,out_path,prop_path):
    all_vids = os.listdir(prop_path)
    out_vids = os.listdir(out_path)
    print(len(all_vids))
    for vid in all_vids:
        if vid not in out_vids:
            csv_name = os.path.join(out_path,vid)
            with open(csv_name,"w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(labels)
            csvfile.close()


def gen_prop(label,out_path,prop_path):
    with open("labels.txt","r") as f:
        tmps = f.readlines()
    labels = []
    labels.append("")
    labels.append("Negative")
    for i in range(len(tmps)):
        tmp = tmps[i].strip()
        labels.append(tmp)
    base = json.load(open(label,"r"))["database"]
    annos = base.keys()
    vid_dict = {}
    for anno in annos:
        vid = anno.split("_")[0]
        pid = anno.split("_")[-1]
        conf = base[anno]["annotations"]["conf"]
        if max(conf)>0:
            conf.insert(0,0)
        else:
            conf.insert(0,1)
        if vid not in vid_dict.keys():
            vid_dict[vid] = {}
        vid_dict[vid][int(pid)] = conf
    
    vids = list(vid_dict.keys())
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    for vid in vids:
        csv_name = os.path.join(out_path,vid+".csv")
        with open(csv_name,"w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(labels)
            pids = range(len(list(vid_dict[vid].keys())))
            for pid in pids:
                confs = vid_dict[vid][pid]
                confs.insert(0,pid)
                writer.writerow(confs)
        csvfile.close()
    make_blanket_output(labels,out_path,prop_path)




    