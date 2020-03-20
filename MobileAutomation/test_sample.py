import subprocess,re,os
'''
device_name=subprocess.check_output("adb shell getprop | grep -e 'ro.product.name' -e 'ro.product.brand", shell=True)
device_name=str(device_name)
print (device_name,type(device_name))
k=re.findall(r'\[(ro.product.brand|ro.product.name)\]: \[(\w{4,20})\]',device_name)
print (k)
name_of_device=k[0][1]+'_'+k[1][1]
print (name_of_device)
'''
os.mkdir('Jenkins')
device_list=subprocess.check_output('adb devices', shell=True)
device_lists=str(device_list).split('List of devices attached')[1].strip()
all_devices_id = re.split(r'(?<=)device',device_lists)
print (os.getcwd())
file=open('device_details.txt','w')
os.chdir('Jenkins')
for deviceid in all_devices_id[:-1]:
        device_id = re.sub(r"[\\n | \\t | \\r]", "", deviceid)
        device_id=deviceid.split("\\n")[-1].split('\\t')[0]
        get_device_name="adb -s {} shell getprop | grep -e 'ro.product.model' -e 'ro.product.brand'".format(device_id)
        print (get_device_name)
        device_name=subprocess.check_output(get_device_name, shell=True)
        device_name=re.sub(r"[\\n | \\t | \\r]", "",str(device_name) )
        k=str(device_name).split('[')
        name_of_device=k[2][:-1]+'_'+k[4][:-2]
        print (name_of_device,k)
        #k=re.findall(r'\[(ro.product.brand|ro.product.model)\]: \[(\w{2,20}|.+\s{2,20}.*)\]',device_name)
        #print (k)
        #name_of_device=k[0][1]+'_'+k[1][1]
        file.write(name_of_device+'  '+device_id+'\n')
        os.mkdir(name_of_device)
        
file.close()