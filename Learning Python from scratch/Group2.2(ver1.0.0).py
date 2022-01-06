import pandas as pd
import os
import multiprocessing
import time

def get_apps(b,e,column=None):
    return get_ds(['E://dataset-app_processes/app_processes.query.{0}.csv'.format(str(i)) for i in range(b,e)],column)
def get_devices(column=None):
    return get_ds(['dataset/devices/'+i for i in os.listdir('dataset/devices')],column)
def get_samples(column=None):
    return get_ds(['dataset/sample/'+i for i in os.listdir('dataset/sample')],column)
def get_ds(files, column=None):
    return pd.concat([read(f, column) for f in files],axis=0)
def read(path, column=None):
    return pd.read_csv(path, delimiter=';', usecols=column, encoding='utf-8', error_bad_lines=False)
def top_20():
    devices = get_devices(['id','brand','model'])
    devices['brand'] = devices['brand'].str.upper()
    models = devices.drop_duplicates(subset=['brand','model'],keep='first',inplace=False)
    brands = models['brand'].value_counts()
    print(brands[:20])
    return brands
def SK(devices,samples):
    sk = 'SAMSUNG'
    id1 = devices[devices['brand']==sk]['id']
    id1 = id1.tolist()
    id2 = samples[samples['device_id'].isin(id1)]['id']
    id2 = id2.tolist()
    return id2

def CN(devices,samples):
    cn = ['LGE', 'HUAWEI', 'TCL', 'ZTE', 'TECNO', 'HTC', 'ASUS', 'OPPO','XIAOMI', 'VIVO']
    id1 = devices[devices['brand'].isin(cn)]['id']
    id1 = id1.tolist()
    id2 = samples[samples['device_id'].isin(id1)]['id']
    id2 = id2.tolist()
    return id2
def G2():
    btime = time.perf_counter() 
    devices = get_devices(['id','brand'])
    devices['brand'] = devices['brand'].str.upper()
    samples = get_samples(['id','device_id'])
    skid = SK(devices,samples)
    cnid = CN(devices,samples)
    del samples,devices
    multi_process(skid,cnid)
    con()
    etime = time.perf_counter()
    print(etime-btime)
    p()
    return 0
def single_process(id1,id2,b,e):
    for i in range(b,e,20):
        count_apps(id1,id2,i,i+20,b)
    count_apps(id1,id2,e-19,e,b)
    return 0
def multi_process(id1,id2):
    processes=[]
    for i in range(1,5913,739):
        processes.append(multiprocessing.Process(target=single_process,args=(id1,id2,i,i+739)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return 0
def count_apps(id1,id2,b,e,prs):
    apps = get_apps(b,e,['sample_id','name'])
    a = apps[apps['sample_id'].isin(id1)]['name'].value_counts()
    b = apps[apps['sample_id'].isin(id2)]['name'].value_counts()
    with open('sk{0}.txt'.format(prs),'a+') as f1:
        f1.writelines(['{0},{1}\n'.format(i,a[i]) for i in a.keys()])
    with open('cn{0}.txt'.format(prs),'a+') as f2:
        f2.writelines(['{0},{1}\n'.format(i,b[i]) for i in b.keys()])
    return a,b
def con():
    skapp={}
    cnapp={}
    for i in range(1,5913,739):
        with open('sk{0}.txt'.format(i),'r') as f:
            for j in f.readlines():
                if j.split(',')[0] in skapp.keys():
                    skapp[j.split(',')[0]] += int(j.split(',')[1][:-1])
                else:
                    skapp[j.split(',')[0]] = int(j.split(',')[1][:-1])
        with open('cn{0}.txt'.format(i),'r') as f:
            for j in f.readlines():
                if j.split(',')[0] in cnapp.keys():
                    cnapp[j.split(',')[0]] += int(j.split(',')[1][:-1])
                else:
                    cnapp[j.split(',')[0]] = int(j.split(',')[1][:-1])
    top_sk= sorted(skapp.items(), key=lambda d:d[1], reverse=True)
    top_cn= sorted(cnapp.items(), key=lambda d:d[1], reverse=True)
    with open('sk.txt','w') as f:
        f.writelines(['{0},{1}\n'.format(i[0],i[1]) for i in top_sk])
    with open('cn.txt','w') as f:
        f.writelines(['{0},{1}\n'.format(i[0],i[1]) for i in top_cn])
    for i in range(1,5913,739):
        os.remove('sk{0}.txt'.format(i))
        os.remove('cn{0}.txt'.format(i))
    return 0
def p():
    with open('sk.txt','r') as f:
        top_sk = f.readlines()
    with open('cn.txt','r') as f:
        top_cn = f.readlines()
    for i in range(20):
        print('sk: {0}cn: {1}'.format(top_sk[i],top_cn[i]))
    return 0
