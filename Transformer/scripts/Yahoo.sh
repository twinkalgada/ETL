export CUDA_VISIBLE_DEVICES=0
folder_name=Test
FILES="/home/tgada/Transformer/thuml-Anomaly-Transformer/data_preprocessing/Yahoo/$folder_name/*.csv"
for f in $FILES
do
  echo "Processing $f file..."
  fbname=${f##*/}
  fbname=${fbname%.csv}
  log_file=Yahoo_logs/$folder_name/$fbname.log
  python data_preprocessing/Yahoo/preprocess.py --file_name $f > $log_file
  anomalous_ratio=0.04
  win_size=5
  python main.py --lr 0.01 --anormly_ratio $anomalous_ratio --win_size $win_size --num_epochs 5   --batch_size 256  --mode train --dataset Yahoo  --data_path dataset/Yahoo/$folder_name/$fbname   --input_c 1  --output_c 1 >> $log_file
  python main.py --lr 0.01 --anormly_ratio $anomalous_ratio --win_size $win_size --num_epochs 5   --batch_size 256     --mode test    --dataset Yahoo   --data_path dataset/Yahoo/$folder_name/$fbname     --input_c 1  --output_c 1 >> $log_file
done
python process_logs.py --anomalous_ratio $anomalous_ratio --win_size $win_size
exit