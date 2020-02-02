__all__ = [
    'get_target_args',
    'build_benchmark_cmd',
    'decode_results',
]

import argparse
import csv
import os.path
import re

from embench_core import log


def get_target_args(remnant):
    """Parse left over arguments"""
    parser = argparse.ArgumentParser(description='Get target specific args')

    parser.add_argument(
        '--ibex-sim',
        type=str,
        required=True,
        help='Path to the Ibex simple system simulator binary',
    )

    return parser.parse_args(remnant)


def build_benchmark_cmd(bench, args):
    """Construct the command to run the benchmark.  "args" is a
       namespace with target specific arguments"""
    cmd = [f'{args.ibex_sim}',
           f'--raminit={bench}']

    return cmd


def decode_results(stdout_str, stderr_str):
    time = re.search('Cycles: *([0-9]+)', stdout_str, re.S)
    if time:
        return float(time.group(1)) / 1000.0
    return 0.0
