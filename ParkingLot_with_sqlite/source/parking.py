import lot_details, car_details
import numpy as np
import sqlite3

conn = sqlite3.connect('parkingLot.db')

class Parking(object):
    """
    Parking class which has details about parking slots
    as well as operation performed on parking are present here
    """

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, no_of_slots):
        
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print ("Parking Lot already created")
            return

        if no_of_slots > 0:
            try:
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS parkingTable(slot_no REAL, reg_no TEXT, colour TEXT, total_time TEXT, charge TEXT)')
                c.close()
            except Exception as ex:
                print("Couldn't make a Table")
            for i in range(1, no_of_slots+1):
                temp_slot = lot_details.PSlot(slot_no=i, available=True)
                self.slots[i] = temp_slot
            print ("Created a parking lot with {} slots" .format(no_of_slots))
        else:
            print ("Number of slots provided is incorrect.")
        return

    def get_nearest_available_slot(self):
        
        available_slots = filter(lambda x: x.available, self.slots.values())
        if not available_slots:
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]

    def park(self, reg_no, colour):

        if not self._do_primary_checks():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            available_slot.car_details = car_details.Car.create(reg_no, colour)
            available_slot.available = False
            try:
                slot_number = available_slot.slot_no
                c = conn.cursor()
                c.execute("INSERT INTO parkingTable VALUES(:slot_no, :reg_no, :colour, :total_time, :charge)",
                {'slot_no':slot_number,'reg_no':reg_no,'colour':colour,'total_time':0,'charge':0})
                conn.commit()
                c.close()
            except Exception as ex:
                print("Couldn't insert data into table")
            print ("Allocated slot number: {}".format(available_slot.slot_no))
        else:
            print ("Sorry, parking lot is full.")

    def leave(self, slot_no, time):

        time = int(time)
        slot_no = int(slot_no)
        if not self._do_primary_checks():
            return
        total_fare = 0
        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car_details:
                pslot.car_details = None
                pslot.available = True
                if time <= 120:
                    total_fare += 30
                else:
                    to_charge = time - 120
                    total_fare+=30
                    total_time = np.ceil(to_charge/60)
                    total_fare+=total_time*10
                try:
                    c = conn.cursor()
                    c.execute("UPDATE parkingTable SET total_time={}, charge={} WHERE slot_no ={}".format(time,total_fare,slot_no))
                    conn.commit()
                    c.close()
                except Exception as ex:
                    print("Couldn't update the table")
                print ("Slot number {} is free. And the charge to the customer is {}".format(slot_no,total_fare))
            else:
                print ("No car is present at slot number {}".format(slot_no))
        else:
            print ("Sorry, slot number does not exist in parking lot.")

    def status(self):

        if not self._do_primary_checks():
            return

        print ("Slot No\tRegistration No\tColour")
        for i in self.slots.values():
            if not i.available and i.car_details:
                print ("{}\t{}\t\t{}".format(i.slot_no, i.car_details.reg_no, i.car_details.colour))
            else:
                print('No Car Present! Please park some car.')
                break

    def _do_primary_checks(self):
        if len(self.slots) == 0:
            print ("Parking Lot not created")
            return False
        return True

    def registration_numbers_for_cars_with_colour(self, colour):

        if not self._do_primary_checks():
            return

        reg_nos = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car_details and \
                pslot.car_details.colour == colour:
                reg_nos += '{}'.format(pslot.car_details.reg_no)

        if reg_nos:
            print ('{}'.format(reg_nos[:-1]))
        else:
            print ("Not found")

    def slot_numbers_for_cars_with_colour(self, colour):

        if not self._do_primary_checks():
            return

        slot_nos = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car_details and \
                pslot.car_details.colour == colour:
                slot_nos += '{} '.format(pslot.slot_no)

        if slot_nos:
            print ('{}'.format(slot_nos))
        else:
            print ("Not found")

    def slot_number_for_registration_number(self, reg_no):

        if not self._do_primary_checks():
            return

        slot_no = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car_details and \
                pslot.car_details.reg_no == reg_no:
                slot_no = pslot.slot_no

        if slot_no:
            print ('{}'.format(slot_no))
        else:
            print ("Not found")
