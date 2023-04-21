# Hàm tính số cách chia thưởng với biến prize (số phần thưởng) và biến member (số học sinh)
def da_wae(prize, member):
    if prize == 0:  # Nếu không có phần thưởng thì có 1 cách chia (không ai được nhận thưởng)
        return 1
    if member == 0:  # Nếu không có học sinh thì có 0 cách chia (bởi không có ai để chia cả :v)
        return 0
    if prize < member: # VD: Cho 3 phần thưởng và có 5 học sinh thì chỉ tặng cho 3 người đầu tiên
        return da_wae(prize, prize)
    if prize >= member:
        # Có 2 trường hợp xảy ra:
        # 1. Mỗi người được nhận 1 phần thưởng, số phần thưởng còn lại chia tiếp cho tất cả học sinh
        # 2. Người cuối không nhận phần thưởng. Phần thưởng chia cho số học sinh trừ đi 1
        return da_wae(prize, member - 1) + da_wae(prize - member, member)


def main():
    prize = abs(int(input("Nhap so phan thuong: ")))
    member = abs(int(input("Nhap so hoc sinh: ")))
    print("Co tat ca", da_wae(prize, member), "cach chia phan thuong")


if __name__ == "__main__":
    main()