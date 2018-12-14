import sqlite3

conn = sqlite3.connect('parkingLot.db')
c = conn.cursor()

def read_whole_database():
    print('{}|{}|    {}| {}| {}'.format('Slot_no','Reg_no','colour','t_time','charge'))
    c.execute("SELECT * FROM parkingTable")

    for row in c.fetchall():
        print(row)

def get_by_reg_no():
    # reg_no = str(reg_no)
    c.execute("SELECT * FROM parkingTable WHERE colour=white ")
    for row in c.fetchall():
        print(row)
read_whole_database()
# get_by_reg_no()