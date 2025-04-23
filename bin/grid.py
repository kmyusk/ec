import datetime
import os
import random

import binutil

from dreamcoder.ec import commandlineArguments, ecIterator
from dreamcoder.grammar import Grammar
from dreamcoder.domains.grid.main import main, grid_options
from dreamcoder.program import Primitive
from dreamcoder.task import Task
from dreamcoder.type import arrow, tint
from dreamcoder.utilities import numberOfCPUs

# import debugpy
# debugpy.listen(("0.0.0.0", 5678))  # NOT "localhost"
# print("Waiting for debugger attach")
# debugpy.wait_for_client()

if __name__ == '__main__':
    args = commandlineArguments(
        enumerationTimeout=10, activation='tanh',
        iterations=10, recognitionTimeout=3600,
        a=3, maximumFrontier=10, topK=2, pseudoCounts=30.0,
        helmholtzRatio=0.5, structurePenalty=1.,
        CPUs=numberOfCPUs(),
        extras=grid_options)
    main(args)
