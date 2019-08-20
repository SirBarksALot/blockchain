# essential modules
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

# PKI modules
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    def __init__(self):
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()


filip = Client
print(filip._public_key, filip._private_key)
