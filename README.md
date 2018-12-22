# reads_depth_normalization
normalize reads depth for `bedtools genomecov` output file

input file format：
chr start_position end_position depth

output file format:
chr start_position end_position normalized_depth

usage：
python reads_depth_normalization.py input_file -O/-output out_dir

example:
python reads_depth_normalization.py exanple/test.txt -O output/

