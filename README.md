# Iranian national code dictionary generator
python script to generate all valid iranian national code by state or city name
## how to use
> 


## use as module
you can use `ir_national_code.py` as module in your python program.

```python
 from ir_national_code import *
 result = ir_national_code() # create object
 result.return_all() #return list of all iranian national code
 result.by_state('فارس') #return list of all of 'فارس' valid national code
 result.by_first_3_digit('001') #return list of all valid nation code start with '001' (choose code from city_codes.json file)
```
also you can change #DO SOMETHING line in `ir_national_code.py` file to do somthing with the generated national code

## TODO
[  ] add json export

[  ] add text export



Tnx to [fandogh](https://github.com/fandogh/codemeli/docs) and [ebraminio](https://gist.github.com/ebraminio/5292017)