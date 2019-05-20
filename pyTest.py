
# import datetime

# t = ('2019-03-18 17:18:42', 10.0)
# # print( t[0][10:16] )

# s = t[0][:10]
# # print(s)
# sp = s.split("-")

# print(sp)
# # new_s = []
# # for n in sp:
# #     new_s.append(n)
# # print(new_s)

# year = int(sp[0])
# month = int(sp[1])
# day = int(sp[2])

# def date_to_day(year, month, day):
#     time = datetime.datetime(year, month, day)
#     return (time.strftime("%a"))

# d = date_to_day(year, month, day)
# print(d)


# monthly processing 
# t = ('2019-03-18 17:18:42', 10.0)
# print( t[0][:7] )

# s = t[0][:10]
# print(s)
# sp = s.split("-")

# year = int(sp[0])
# month = int(sp[1])
# day = int(sp[2])

# # def month_from_full_date(year, month, day):
# #     time = datetime.datetime(year, month, day)
# #     return (time.strftime("%y"))

# # d = month_from_full_date(year, month, day)
# # print(d)

# print(year)

# mydate = datetime.datetime.now()
# print(mydate)
# m = mydate.strftime("%B")
# print(m)

# import statistics as stat

temp1 = [30.4, 45.5, 40.7, 47.2, 42.7, 44.1, 35.8, 37.8, 36.3, 36.3, 35.6]
temp2 = [33.4, 33.5, 41.7, 11.2, 2.7, 3.1, 55.8, 77.8, 36.3, 66.3, 25.6]


print('last temp..', temp1[-5:])
print('prev_temp..', temp1[-10:-5])

lsum = sum(temp1[-5:])
psum = sum(temp1[-10:-5])
c = lsum - psum
pc = (c/lsum) * 100
print(round(pc,2))

print('min...', min(temp1))

print(temp1[-1])
l = ['temp : 2', 'turb: 23', 'ph: 5', 'water_level: 33']


{
    "temp":2, 
}

print( l[1].split(':')[0] )
# print("mean: ", round(mean, 2))

# print(c,"%")