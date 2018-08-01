'''
编写用户转账函数，实现功能
		1、传入源账户名（保证必须为str）、目标账户名（保证必须为str）、转账金额（保证必须为数字）
		2、实现源账户减钱，目标账户加钱
'''
# Demo1/Homework/day10/bank_info
def Transfer():
    old_info_number = -1
    new_info_number = -1
    old_account = input('源用户名：')
    new_account = input('新用户名：')
    amount = input('转账金额：')
    if not old_account.isnumeric() and not new_account.isnumeric():
        print('帐户名必须为数字')
        return False
    if not amount.isnumeric():
        print('转账金额必须为数字！')
        return False
    with open('bank_info', 'r', encoding='utf-8') as info:
        lines  =info.readlines()
    for i in range(len(lines)):
        if old_account == lines[i].split('|')[0]:
            old_info_number = i
        if new_account == lines[i].split('|')[0]:
            new_info_number = i
    old_info_list = lines[old_info_number].split('|')
    new_info_list = lines[new_info_number].split('|')
    old_info_list[2] = str(float(old_info_list[2].strip('\n')) - float(amount)) + '\n'
    new_info_list[2] = str(float(new_info_list[2].strip('\n')) + float(amount)) + '\n'
    lines[old_info_number] = '|'.join(old_info_list)
    lines[new_info_number] = '|'.join(new_info_list)
    with open('bank_info', 'w', encoding='utf-8') as info:
        info.writelines(lines)
    return True
Transfer()