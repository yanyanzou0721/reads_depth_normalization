# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:56:18 2018

@author: zou
"""

import pandas as pd
import numpy as np
import os
import click
import logging
from sys import stderr
from os.path import join, exists

log = logging.getLogger(__name__)

def f(x):
    return x['depth']

@click.command(name="reads_depth_normalization")
@click.argument("input_txt")
@click.option("--outdir", "-O",
    default="./",
    help="path to output files.")


def main_(input_txt, outdir):

    if not exists(outdir):
        os.mkdir(outdir)
     
    data = pd.read_table(input_txt,names=['chr','start','end','depth'])
    data['nor_depth']=((data.apply(f,axis=1))/data['depth'].mean())*100
    data=data.drop('depth',axis=1)
    out_path=outdir+'/'+input_txt
    data.to_csv(out_path,header=0,sep=' ',index=0)
    msg = "sample reads depth: {} 's normalization result will store to {}".format(
            input_txt, out_path )
    log.info(msg)
    

if __name__ == "__main__":
    log.setLevel(logging.DEBUG)
    hdr = logging.StreamHandler(stream=stderr)
    fmt = logging.Formatter(
        fmt="[%(levelname)s][%(asctime)s] %(message)s",
        datefmt="%m/%d/%y %H:%M:%S")
    hdr.setFormatter(fmt)
    log.addHandler(hdr)
    main_()

