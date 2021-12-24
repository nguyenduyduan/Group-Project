def nhap_du_lieu_so():
    kt=False
    while kt==False:
        try:
            n=int(input())
            return n
        except:
            print('Dữ liệu là một số, hãy nhập lại:')

def kiem_tra_tien(hm,stcl):
    if stcl==0:
        print('Bạn đã sử dụng hết hạn mức đề ra')
    elif stcl<0.05*hm:
        print('Số tiền còn lại của bạn đã dưới 5% hạn mức tiêu dùng')
    elif stcl<0.1*hm:
        print('Số tiền còn lại của bạn đã dưới 10% hạn mức tiêu dùng')

def chi_tieu(stcl,thong_ke, tongtien):
    ten=str(input('Nhập tên chi phí: '))
    print('Nhập chi phí phải bỏ ra: ')
    cp=nhap_du_lieu_so()
    if cp>stcl:
        print('Chi phí lớn hơn hạn mức mất rồi, bạn cần lựa chọn 1 trong 2 phương án sau:')
        print(' \n1.Từ bỏ việc chi tiêu này')
        print('2.Mở rộng hạn mức để đủ cho chi phí này (điều này sẽ làm bạn vượt quá giới hạn chi tiêu)')
        print('Lựa chọn phương án:')
        n=lua_chon(2)
        if n==2:
            mo_rong=cp-stcl
            print('Bạn cần mở rộng thêm:',mo_rong)
            if mo_rong>tongtien :
                print('Bạn không đủ tiền cho khoản chi phí này')
                print('=> Từ bỏ nhé')
            else:
                print('Bạn đã vượt hạn mức:',mo_rong)
                thong_ke.append([ten,-cp])
                return mo_rong,cp,1 #1 là số lần mở rộng hạn mức
        else:
            print('Bạn đã lựa chọn từ bỏ việc chi tiêu này')
    else:
        thong_ke.append([ten,-cp])
    return 0,cp,0

def thu_nhap(tongtien,luong,thong_ke):
    print(' \n1.Nhận lương \n2.Thu nhập khác')
    print('Lựa chọn trường hợp')
    n=lua_chon(2)
    if n==1:
        tongtien+=luong
        thong_ke.append(['lương cố định',luong])
    else:
        ten=str(input('Nhập tên khoản thu nhập này:'))
        #Khoản này có thể là nhặt được hoặc trúng thưởng hoặc được ai đó cho.
        print('Nhập số tiền (đơn vị là VND):')
        tien=nhap_du_lieu_so()
        tongtien+=tien
        thong_ke.append([ten,tien])
    return tongtien

def lua_chon(n):
    m=nhap_du_lieu_so()
    luachon=[]
    for i in range(n):
        luachon.append(i+1)
    while m not in luachon:
        print('Chỉ nhập 1 số từ 1 đến {}:'.format(n))
        m=nhap_du_lieu_so()
    return m

#--------------------------------------
print('Chương trình quản lý chi tiêu của Shopeer')
s=str(input('Nhập tên người dùng: '))
print('Chào mừng {} đã đến với chương trình của chúng tôi'.format(s))

print('Nhập số tiền hiện có của bạn (đơn vị là VND):')
tongtien=nhap_du_lieu_so()
print('Nhập tiền lương mỗi tháng của bạn (đơn vị là VND):')
luong=nhap_du_lieu_so()
print('Nhập vào hạn mức chi tiêu của bạn đặt ra trong tháng (đơn vị là VND):')
hm=nhap_du_lieu_so()
while hm>tongtien or hm>luong:
    print('Hạn mức không được lớn hơn tổng số tiền hiện có và không được lớn hơn lương')
    print('hãy nhập lại hạn mức (đơn vị là VND):')
    hm=nhap_du_lieu_so()
stcl=hm #Đây là số tiền còn lại mà người dùng có thể chi tiêu theo hạn mức đã đặt ra
tongtien-=hm #Đây là tổng số tiền còn lại, không kể hạn mức chi tiêu đặt ra
thong_ke=[]
dem=0 #số lần mở rộng hạn mức
vuot_hm=0
for i in range(1,4):
    print('Ngày thứ',i,'\n ')
    kt=False
    while kt==False:
        print('1:Thu nhập \n2:Chi phí \n3:Thống kê những ngày qua \n4:Kết thúc ngày')
        print(' \nNhập các số theo các trường hợp')
        n=lua_chon(4)
        if n==1:
            tongtien=thu_nhap(tongtien, luong, thong_ke)
        elif n==2:
            mo_rong,cp,d=chi_tieu(stcl,thong_ke,tongtien)
            vuot_hm+=mo_rong
            tongtien-=mo_rong
            stcl-=(cp-mo_rong)
            dem+=d
            kiem_tra_tien(hm,stcl)
        elif n==3:
            for i in range(len(thong_ke)):
                print('{} : {}'.format(thong_ke[i][0],thong_ke[i][1]))
        else:
            print('Kết thúc 1 ngày')
            print('Hạn mức tiêu dùng còn lại là:',stcl)
            print('------------------------------')
            break

print('Tổng kết tháng')
if dem==0:
    if stcl > 0:
        print('THÔNG BÁO: Bạn đã chi tiêu ít hơn hạn mức. Chúc mừng {} đã có một tháng chi tiêu tiết kiệm'.format(s))
    elif stcl == 0:
        print('THÔNG BÁO: Bạn đã chi tiêu vừa bằng hạn mức. Xin chúc mừng')
else:
    print('THÔNG BÁO: Bạn đã chi tiêu vượt quá hạn mức {} lần với số tiền là {}'.format(dem,vuot_hm))
print('Tổng số tiền còn lại là',tongtien+stcl)
print(' \nThống kê hoạt động tháng này:')
for i in range(len(thong_ke)):
    print('{} : {}'.format(thong_ke[i][0],thong_ke[i][1]))
