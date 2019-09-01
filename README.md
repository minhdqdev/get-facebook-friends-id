# get-facebook-friends-id
Get all fbid of your friends with Selenium

## Getting Started
### Step 1: Setup
- Install `Selenium` and geckodriver for Firefox.
- Install `BeautifulSoup`

### Step 2: Config
- Copy `sample_user_config.json` to a new file `user_config.json`.
- Replace the user and password.

### Step 3: Use
- Run `get_fbid.py` or `get_fbid_better.py`. You can see the different in result of 2 files in the Benchmark section.

## Benchmark
### 1. Use facebook. no GUI
```
time python get_fbid.py
```

```
real    0m48.206s
user    0m52.522s
sys     0m5.680s
```

friendlist: 349

### 2. Use Facebook Mobile, no GUI
```
time python get_fbid_better.py
```

```
real    0m23.611s
user    0m12.344s
sys     0m2.572s
```

friendlist: 287

Ground truth: 389

### Conclusion
You should use the first method because it has a better result, which is more important than time optimization. 
