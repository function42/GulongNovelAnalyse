# -*- coding: utf-8 -*-
# In[1]
import os
import utils

utils.echo()

# In[2]
if(not(os.path.exists("./data"))):
	os.mkdir("./data")
if(not(os.path.exists("./data/books"))):
	os.mkdir("./data/books")
if(not(os.path.exists("./data/links"))):
	os.mkdir("./data/links")