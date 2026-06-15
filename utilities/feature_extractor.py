def extract_features(url):
    # Trích xuất đặc trưng từ URL
    features = [ len(url), # URL length 
                url.count('.'), # dots 
                url.count('/'), # slashes 
                url.count('-'), # hyphens 
                url.count('@'), # @ symbols 
                url.count('?'), # question marks 
                url.count('='), # equal signs 
                url.count('%'), # percent signs 
                int('https' in url), # https present
                int('www' in url) # www present 
                ]
    return features