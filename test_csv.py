# coding=utf-8

import csv
import os

dir_x = 10
source_dir = 'E:\\TSA\\1031\\1031\\%s'% dir_x
result_dir = 'E:\\TSA\\1031\\1031_result\\%s'% dir_x


def begin_fix():
    source_file_name_list = os.listdir((source_dir))
    for source_file_name in source_file_name_list:
        source_file_path = os.path.join(source_dir,source_file_name)
        print (source_file_path)
        result_file_name_path = os.path.join(result_dir,source_file_name)
        print (result_file_name_path)
        fix_csv(source_file_path,result_file_name_path)
        #break


def fix_csv(source_path,result_path):
    with open(source_path) as csvfile:
        i = 0
        csv_reader = csv.reader((line.replace('\0', '') for line in csvfile))
        #csv_reader = csv.reader(csvfile)
        list = []
        for row in csv_reader:
            if row:
                new_row = []
                new_row.append(row[0])
                new_row.append(row[2])
                new_row.append(row[4])
                new_row.append(row[6])
                new_row.append(row[7])
                new_row.append(row[8])
                new_row.append(row[9])
                new_row.append(row[20])
                new_row.append(row[21])
                list.append(new_row)
            else:
                break

    with open(result_path,"w", newline='') as out:
        for row in list:
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow(row)





if __name__ == '__main__':
    begin_fix()