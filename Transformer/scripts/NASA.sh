export CUDA_VISIBLE_DEVICES=0

python main.py --anormly_ratio 0.07 --win_size 125 --num_epochs 10   --batch_size 128  --mode train --dataset NASA  --data_path dataset/NASA   --input_c 7  --output_c 7
python main.py --anormly_ratio 0.07 --win_size 125 --num_epochs 10   --batch_size 128     --mode test    --dataset NASA   --data_path dataset/NASA     --input_c 7  --output_c 7