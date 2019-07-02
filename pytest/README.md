#  pytest
*   running test 
    * py.test test_sample.py
* running test with mark 
    * py.test {tes_file_name}-m  {mark name}
      *  e.g py.test test_sample_mark.py -m set1
* result XML
    * py.test test_sample_skip.py -v --junitxml="result.xml"