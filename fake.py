
từ bs4 nhập BeautifulSoup
từ datetime nhập datetime
nhập lại, yêu cầu, hệ điều hành, hệ thống
từ thời gian nhập khẩu giấc ngủ
từ ngày giờ nhập ngày
yêu cầu nhập khẩu, ngẫu nhiên
yêu cầu nhập khẩu
nhập base64, json, os
từ ngày giờ nhập ngày
từ datetime nhập datetime
từ thời gian nhập sleep, strftime
từ bs4 nhập BeautifulSoup
từ datetime nhập datetime
nhập lại, yêu cầu, hệ điều hành, hệ thống
từ thời gian nhập khẩu giấc ngủ
từ ngày giờ nhập ngày
yêu cầu nhập khẩu, ngẫu nhiên
nhập uuid, re
từ bs4 nhập BeautifulSoup
ổ cắm nhập khẩu
từ datetime nhập datetime
thời gian=ngàygiờ.bây giờ().strftime("%H:%M:%S")
từ pystyle import *
máy_dữ_liệu = []
hôm nay = ngày.hôm nay()
bây giờ = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
nhập khẩu ngẫu nhiên
yêu cầu nhập khẩu
nhập base64
từ pystyle nhập Màu sắc, Tô màu, Trung tâm
nền tảng nhập khẩu
từ datetime nhập datetime, timedelta
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
làm = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
thanh = f'{vang[{xanh_la</>{vang}] {tim}=> '


lớp CanCuocCongDan:
    định nghĩa __init__(bản thân):
        self.province_codes = {
            "Hà Nội": "001",
            "Hà Giang": "002",
            "Cao Bằng": "004",
            "Bắc Kạn": "006",
            "Tuyên Quang": "008",
            "Lào Cai": "010",
            "Điện Biên": "011",
            "Lai Châu": "012",
            "Sơn La": "014",
            "Yên Bái": "015",
            "Hòa Bình": "017",
            "Thái Nguyên": "019",
            "Lạng Sơn": "020",
            "Quảng Ninh": "022",
            "Bắc Giang": "024",
            "Phú Thọ": "025",
            "Vĩnh Phúc": "026",
            "Bắc Ninh": "027",
            "Hải Dương": "030",
            "Hải Phòng": "031",
            "Hưng Yên": "033",
            "Thái Bình": "034",
            "Hà Nam": "035",
            "Nam Định": "036",
            "Ninh Bình": "037",
            "Thanh Hóa": "038",
            "Nghệ An": "040",
            "Hà Tĩnh": "042",
            "Quảng Bình": "044",
            "Quảng Trị": "045",
            "Thừa Thiên Huế": "046",
            "Đà Nẵng": "048",
            "Quảng Nam": "049",
            "Quảng Ngãi": "051",
            "Bình Định": "052",
            "Phú Yên": "054",
            "Khánh Hòa": "056",
            "Ninh Thuận": "058",
            "Bình Thuận": "060",
            "Kon Tum": "062",
            "Gia Lai": "064",
            "Đắk Lắk": "066",
            "Đắk Nông": "067",
            "Lâm Đồng": "068",
            "Bình Phước": "070",
            "Tây Ninh": "072",
            "Bình Dương": "074",
            "Đồng Nai": "075",
            “Bà Rịa - Vũng Tàu”: “077”,
            "Hồ Chí Minh": "079",
            "Long An": "080",
            "Tiền Giang": "082",
            "Bến Tre": "083",
            "Trà Vinh": "084",
            "Vĩnh Long": "086",
            "Đồng Tháp": "087",
            "An Giang": "089",
            "Kiên Giang": "091",
            "Cần Thơ": "092",
            "Hậu Giang": "093",
            "Sóc Trăng": "094",
            "Bạc Liêu": "095",
            "Cà Mau": "096"
        }

    def generate_random_number(self, issue_date):
        thử:
            ngày_phát_hành = datetime.strptime(ngày_phát_hành, "%d/%m/%Y")
            ngày_trong_năm = ngày_phát_hành.timetuple().tm_yday
            nếu ngày_trong_năm < 180:
                num = ngẫu nhiên.randint(100, 99999)
            khác:
                num = ngẫu nhiên.randint(99999, 999999)
            trả về str(num).zfill(6)
        ngoại trừ ValueError:
            trả về Không có

    def calculate_issue_and_expiry_dates(self, birth_date_str):
        thử:
            ngày_sinh = datetime.strptime(ngày_sinh_str, "%d/%m/%Y")
        ngoại trừ ValueError:
            return {"status": "false", "msg": "Ngày sinh không hợp lệ."}
        
        current_date = datetime.now()
        tuổi = (ngày hiện tại - ngày sinh).ngày // 365

        nếu tuổi < 14:
            return {"status": "false", "msg": "Công dân chưa đủ tuổi để cấp thẻ CCCD."}
        randay = ngẫu nhiên.randint(30,90)
        nếu 14 <= ​​tuổi < 25:
            tuổi_hết_hạn = 25
            ngày_phát_hành = ngày_sinh + timedelta(ngày=14*365 + randay)
        elif 25 <= tuổi < 40:
            tuổi_hết_hạn = 40
            ngày_phát_hành = ngày_sinh + timedelta(ngày=25*365 + randay)
        nếu 40 <= tuổi < 60:
            tuổi_hết_hạn = 60
            ngày_phát_hành = ngày_sinh + timedelta(ngày=40*365 + randay)
        khác:
            expiry_age = Không có
            ngày_phát_hành = ngày_sinh + timedelta(ngày=60*365 + randay)
            
        nếu expiration_age:
            tach = str(ngày_sinh_str).split('/')
            so_cuoi = int(đính kèm[-1]) + tuổi_hết_hạn
            ngày_hết_hạn = tach[0] + '/' + tach[1] + '/' + str(so_cuoi)
        khác:
            Expired_date = "Thẻ CCCD có giá trị suốt đời"

        ngày_phát_hành = ngày_phát_hành.strftime("%d/%m/%Y")
        hết hạn_date_str = hết hạn nếu hết hạn_date != "Thẻ CCCD có giá trị suốt đời" else hết hạn_date

        trở lại {
            "trạng thái": "đúng",
            "Thẻ cấp ngày": issue_date_str,
            "Hạn thẻ": Expired_date_str
        }

    def generate_cccd(self, province_name, gender, birth_date_str, issue_date_str):
        mã_tỉnh = self.mã_tỉnh.lấy(tên_tỉnh)
        nếu không phải là mã_tỉnh:
            return {"status": "false", "msg": "Tên tỉnh không hợp lệ."}

        nếu giới tính không nằm trong ["Nam", "Nữ"]:
            return {"status": "false", "msg": "Giới tính không hợp lệ."}

        thử:
            ngày_sinh = datetime.strptime(ngày_sinh_str, "%d/%m/%Y")
        ngoại trừ ValueError:
            return {"status": "false", "msg": "Ngày sinh không hợp lệ."}

        năm_sinh = ngày_sinh.năm

        nếu năm sinh < 1900 hoặc năm sinh > 2099:
            return {"status": "false", "msg": "Năm sinh không hợp lệ."}

        nếu năm sinh < 2000:
            gender_code = 0 nếu giới tính == "Nam" nếu không thì 1
        khác:
            gender_code = 2 nếu giới tính == "Nam" nếu không thì 3

        mã_năm_sinh = chuỗi(năm_sinh)[-2:]
        random_number = self.generate_random_number(issue_date_str)

        nếu không phải là random_number:
            return {"status": "false", "msg": "Ngày cấp thẻ không hợp lệ."}

        cccd = f"{mã_tỉnh}{mã_giới_tính}{mã_năm_sinh}{số_ngẫu_nhiên}"
        trả về {"trạng thái": "đúng", "socccd": cccd}

    def Create(bản thân, giới tính, ngày sinh, tên tỉnh):
        ngày = self.calculate_issue_and_expiry_dates(birth_date_str)
        nếu dates['status'] != 'true':
            ngày trở về

        cccd = self.generate_cccd(tỉnh_name, giới tính, ngày sinh_str, ngày['Ngày cấp thẻ'])
        nếu cccd['status'] != 'true':
            trả lại cccd
        khác:
            trả về cccd, ngày tháng
def clear():
    os.system("cls" nếu os.name == "nt" nếu không thì "xóa")
# hàm chống bug
def validate_non_empty(prompt):
    trong khi Đúng:
        giá trị = đầu vào(prompt).strip()
        nếu giá trị:
            giá trị trả về
        khác:
            print("Lỗi: Trường hợp này không thể trống. Vui lòng nhập lại.")

def validate_date(prompt):
    trong khi Đúng:
        date_str = đầu vào(prompt).strip()
        nếu không phải là date_str:
            print("Lỗi: Trường hợp này không thể trống. Vui lòng nhập lại.")
            Tiếp tục
        thử:
            trả về datetime.strptime(date_str, "%d/%m/%Y")
        ngoại trừ ValueError:
            print("Lỗi: Ngày không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")

def validate_gender(prompt):
    trong khi Đúng:
        giới tính = đầu vào (lời nhắc). viết hoa (). dải ()
        nếu không phải giới tính:
            print("Lỗi: Trường hợp này không thể trống. Vui lòng nhập lại.")
        giới tính elif trong ["Nam", "Nữ"]:
            trả về giới tính
        khác:
            print("Lỗi: Giới tính không hợp lệ. Chỉ nhập 'Nam' hoặc 'Nữ'.")

def validate_socccd(prompt):
    trong khi Đúng:
        socccd = đầu vào(prompt).strip()
        nếu không phải là socccd:
            print("Lỗi: Trường hợp này không thể trống. Vui lòng nhập lại.")
        elif (socccd.isdigit() và len(socccd) == 12):
            trả lại socccd
        khác:
            print("Lỗi: Số CCCD không hợp lệ. Nhập 12 chữ số.")

def validate_province(prompt, valid_provinces):
    trong khi Đúng:
        tỉnh = đầu vào (lời nhắc). tiêu đề (). dải ()
        nếu không phải là tỉnh:
            print("Lỗi: Trường hợp này không thể trống. Vui lòng nhập lại.")
        đối với prv ở valid_provinces:
            nếu prv ở tỉnh:
                trở về tỉnh
        print("Lỗi: Tên tỉnh/thành phố không hợp lệ. Vui lòng nhập lại.")

def validate_url(prompt):
    trong khi Đúng:
        url = đầu vào(lời nhắc).dải()
        nếu không phải là url:
            print("Lỗi: Trường hợp này không thể trống. Vui lòng nhập lại.")
        elif requests.utils.urlparse(url).scheme trong ['http', 'https']:
            trả về url
        khác:
            print("Lỗi: Liên kết không hợp lệ. Vui lòng nhập một hợp lệ URL bắt đầu bằng http hoặc https.")

tùy chọn gradient = [
    Màu sắc.đỏ_đến_vàng,
    Màu sắc.xanh lá cây_sang_xanh lam,
    Màu sắc.tím_đến_đỏ,
    Màu sắc.vàng_đến_đỏ,
    Màu sắc.xanh lam đến tím,
    Màu sắc.cầu vồng,
]

def banner():
    os.system("cls" nếu os.name == "nt" nếu không thì "xóa")
    os_type = platform.system()
    os_text = f"Hệ điều hành: {os_type}"

    # Banner ASCII # Tool by cao cấp, Không xóa dòng này để tôn vinh tác giả.
    ascii = """
           © BẢN QUYỀN CỦA PHƯỚC AN + BVZONE 2025

███████╗░██╗░░░██╗████████╗░█████╗░░████╗░████╗░░░░░
██╔══██╗███║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░
██████╦╝╚██╗░██╔╝░░░██║░░░██║░░██║░██║░██║░█║░█║░░░░
██╔══██╗░╚█████╔╝░░░░░██║░░░██║░░██║░██║░██║░█║░░░░░
███████╦╝░░╚██╔╝░░░░░░██║░░░╚████╔╝╚█████╔╝███████╗
╚═════╝░░░░╚═╝░░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░╚═════╝

"""

    # Màu ngẫu nhiên
    gradient = random.choice(gradient_options)
    colored_ascii = Tô màu.Dọc(gradient, ascii)
    cho dòng trong colored_ascii.splitlines():
        in(Center.XCenter(dòng))


    # Trích dẫn sự kiện
    
    in(Center.XCenter(Tô màu.Ngang(gradient, f"\n{os_text}")))
    print(Center.XCenter(Colorate.Horizontal(gradient, "🔗 Hộp Zalo: https://zalo.me/g/bhbotm174\n")))
    print(Center.XCenter(Colorate.Horizontal(gradient, "🔗 Admin: Phạm An Phước + Trần Dương Ngọc Thành\n")))

thông thoáng()
ngọn cờ()
option = valid_non_empty(f"{thanh}\033[1;37mCó muốn tự động tạo số CCCD không tạo có thể trùng lặp với người thật (Y/n):{tim} ")
nếu option.lower() != 'y':
    name = valid_non_empty(f"{thanh}\033[1;37mNhập Tên:{tim} ")
    socccd = valid_socccd(f"{thanh}\033[1;37mNhập Số CCCD:{tim} ")
    sinh nhật = valid_date(f"{thanh}\033[1;37mNhập Ngày Sinh (dd/mm/yyyy):{tim} ")
    sex = valid_gender(f"{thanh}\033[1;37mNhập Giới Tính (Nam/Nữ):{tim} ")
    quequan = valid_province(f"{thanh}\033[1;37mNhập Quê Quán ( Ví dụ: Thị trấn Đình Cả, Võ Nhai, Thái Nguyên ):{tim}", CanCuocCongDan().province_codes)
    hangtren = valid_non_empty(f"{thanh}\033[1;37mNhập Hàng Trên Nơi Nơi Thường Trú ( Ví dụ: 30/18/19, Thống ) (Bỏ Qua Gõ None):{tim} ")
    hangduoi = valid_province(f"{thanh}\033[1;37mNhập Hàn dưới Nơi Thường Trú ( Ví dụ: Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    thuongtru = valid_province(f"{thanh}\033[1;37mNhập Nơi Thường Trú Đầy ( Ví dụ: 30/18/19, Thống Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    noisinh = valid_province(f"{thanh}\033[1;37mNhập Nơi Sinh ( Ví dụ: Thái Nguyên ):{tim} ", CanCuocCongDan().province_codes)
    ngaycap = valid_date(f"{thanh}\033[1;37mNhập Ngày Cấp (dd/mm/yyyy):{tim} ")
    thoihan = valid_date(f"{thanh}\033[1;37mNhập Thời Gian (dd/mm/yyyy):{tim} ")
    anhthe = validation_url(f"{thanh}\033[1;37mNhập Link Ảnh Tag:{tim} ")
    thông thoáng()
    in(banne)
khác:
    socccd = 'tự động'
    ngaycap = 'tự động'
    thoihan = 'tự động'
    name = valid_non_empty(f"{thanh}\033[1;37mNhập Tên:{tim} ")
    sinh nhật = valid_date(f"{thanh}\033[1;37mNhập Ngày Sinh (dd/mm/yyyy):{tim} ")
    sex = valid_gender(f"{thanh}\033[1;37mNhập Giới Tính (Nam/Nữ):{tim} ")
    quequan = valid_province(f"{thanh}\033[1;37mNhập Quê Quán ( Ví dụ: Thị trấn Đình Cả, Võ Nhai, Thái Nguyên ):{tim}", CanCuocCongDan().province_codes)
    hangtren = valid_non_empty(f"{thanh}\033[1;37mNhập Hàng Trên Nơi Nơi Thường Trú ( Ví dụ: 30/18/19, Thống ) (Bỏ Qua Gõ None):{tim} ")
    hangduoi = valid_province(f"{thanh}\033[1;37mNhập Hàn dưới Nơi Thường Trú ( Ví dụ: Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    thuongtru = valid_province(f"{thanh}\033[1;37mNhập Nơi Thường Trú Đầy ( Ví dụ: 30/18/19, Thống Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    noisinh = valid_province(f"{thanh}\033[1;37mNhập Nơi Sinh ( Ví dụ: Thái Nguyên ):{tim} ", CanCuocCongDan().province_codes)
    anhthe = validation_url(f"{thanh}\033[1;34mNhập Link Ảnh Tag:{tim} ")
    thông thoáng()
    in(banne)
can_cuoc = CanCuocCongDan()
res = can_cuoc.Create(sex, birthday.strftime("%d/%m/%Y"), noisinh)
nếu isinstance(res, dict) và res.get('status') == 'false':
    print("Lỗi: ", res['msg'])
khác:
    nếu isinstance(res, tuple) và len(res) == 2:
        cccd, ngày tháng = res
    khác:
        print("Lỗi: Không thể tạo CCCD. Đã nhận được kết quả không được mong đợi.")
        ra()

    nếu socccd == 'tự động':
        socccd = cccd['socccd']
    nếu ngaycap == 'auto':
        ngaycap = ngày['Thẻ cấp ngày']
    nếu thoihan == 'tự động':
        thoihan = ngày['Hạn thẻ']
    
    print("Đang Tạo ...")
    phản hồi = yêu cầu. bài đăng ("https://nguyenxuantrinh.id.vn/fake-cccd/api.php", dữ liệu = {
        "tên": tên,
        "socccd": soccd,
        "sinh nhật": birthday.strftime("%d/%m/%Y"),
        "sex": tình dục,
        "quequan": quequan,
        "hangtren":hangtren,
        "hangduoi": hangduoi,
        "thuongtru": thuongtru,
        "ngaycap": ngaycap,
        "thoihan": thoihan,
        "anhthe": anhthe
    }).json()

    trạng thái = phản hồi["trạng thái"]
    in(phản hồi["tin nhắn"])
    nếu trạng thái != "thành công":
        ra()
    với open("mat_truoc.jpeg", "wb") là f:
        f.write(base64.b64decode(response.get("mattruoc", "")))
    với open("mat_sau.jpeg", "wb") là f:
        f.write(base64.b64decode(response.get("matsau", "")))
    print("Đã Lưu Vào File mattruoc.jpeg và matsau.jpeg")




