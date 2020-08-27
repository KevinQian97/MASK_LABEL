python gkang2json.py --prop_dir "/home/diva/kf1_split2_test_new/proposals" \
    --out_dir "./json/test"

python align.py --prop-path ./json/train --gt-path ./gt/trn --out-path ./mask_align_trn.json
python anno_gen.py --train data/kf1_test_align.json --val="" --out data/test_anno.json --all