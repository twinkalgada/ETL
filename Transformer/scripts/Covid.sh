export CUDA_VISIBLE_DEVICES=0

python main.py --anormly_ratio 0.03 --win_size 40 --num_epochs 10   --batch_size 128  --mode train --dataset Covid  --data_path dataset/COVID   --input_c 1  --output_c 1
python main.py --anormly_ratio 0.03 --win_size 40 --num_epochs 10   --batch_size 128     --mode test    --dataset Covid   --data_path dataset/COVID     --input_c 1 --output_c 1