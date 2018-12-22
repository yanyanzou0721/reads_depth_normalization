# reads_depth_normalization
normalize reads depth for `bedtools genomecov` output file

## input file format：
```
chr start_position end_position depth
NC_000962.3     0       1       251
NC_000962.3     1       3       252
NC_000962.3     3       4       254
NC_000962.3     4       11      258
NC_000962.3     11      13      264
NC_000962.3     13      14      266
NC_000962.3     14      15      267
```

##output file format:
```
chr start_position end_position normalized_depth
NC_000962.3     0       1       89.4511760513186
NC_000962.3     1       3       89.80755523877406
NC_000962.3     3       4       90.52031361368495
NC_000962.3     4       11      91.94583036350676
NC_000962.3     11      13      94.08410548823947
NC_000962.3     13      14      94.79686386315038
NC_000962.3     14      15      95.15324305060584
```

##usage：
```
python reads_depth_normalization.py input_file -O/-outdir out_dir

Options:
	  -O, --outdir TEXT       path to output file.
```

##example:
```
python reads_depth_normalization.py exanple/test.txt -O output/
```

