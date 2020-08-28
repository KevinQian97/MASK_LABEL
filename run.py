import os
import json
from pred_prop import gen_prop
import argparse

def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_dir', type=str, required=False, help='Path to location of training proposals')
    parser.add_argument('--test_dir', type=str, required=False, help='Path to location of testing of proposals')
    # parser.add_argument('--prop_lst', type=str,default='out.json', help='final json file in NIST format')
    parser.add_argument('--out_dir', type=str,default='./result', help='prop meta info dir')
    return parser.parse_args()

if __name__ == '__main__':
    config = parse_opts()
    # if os.path.exists("./json/train"):
    #     os.system("rm -r ./json/train/*")
    # if os.path.exists("./json/test"):
    #     os.system("rm -r ./json/test/*")
    # call = "python gkang2json.py --prop_dir {} --out_dir ./json/train".format(config.train_dir)
    # os.system(call)
    # call = "python gkang2json.py --prop_dir {} --out_dir ./json/test".format(config.test_dir)
    # os.system(call)
    # print("Successfully generate json format output")
    # print("Now start making alignments for training proposals")
    # call = "python align.py --prop-path ./json/train --gt-path ./gt/trn --out-path ./mask_align_trn.json"
    # os.system(call)
    # print("Successfully generate alignments for training proposals")
    # print("Now start making alignments for testing proposals")
    # call = "python align.py --prop-path ./json/test --gt-path ./gt/tst --out-path ./mask_align_tst.json"
    # os.system(call)
    # print("Successfully generate alignments for testing proposals")
    # call = "python anno_gen.py --train ./mask_align_trn.json --val="" --out ./mask_anno_trn.json --all"
    # os.system(call)
    # call = "python anno_gen.py --train ./mask_align_tst.json --val="" --out ./mask_anno_tst.json --all"
    # os.system(call)
    gen_prop("./mask_anno_trn.json",os.path.join(config.out_dir,"trn_labels"),config.train_dir)
    gen_prop("./mask_anno_tst.json",os.path.join(config.out_dir,"tst_labels"),config.test_dir)
    print("Finish")

    

    
