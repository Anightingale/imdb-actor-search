# distributing tests within module itself often increases complexity for users; many test suites often require additional dependencies and runtime contexts.

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import imdb_actor_search