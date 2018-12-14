import lot_details, car_details

class Parking(object):

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, no_of_slots):
        
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print ("Parking Lot already created")
            return

        if no_of_slots > 0:
            for i in range(1, no_of_slots+1):
                temp_slot = lot_details.PSlot(slot_no=i,
                                    available=True)
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
            print ("Allocated slot number: {}".format(available_slot.slot_no))
        else:
            print ("Sorry, parking lot is full.")

    def leave(self, slot_no):

        slot_no = int(slot_no)
        if not self._do_primary_checks():
            return

        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car_details:
                pslot.car_details = None
                pslot.available = True
                print ("Slot number {} is free".format(slot_no))
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
                reg_nos += '%s ' % pslot.car_details.reg_no

        if reg_nos:
            print ('{}'.format(reg_nos[:-1]))
        else:
            print ("Not found")

    def slot_numbers_for_cars_with_colour(self, colour):

        if not self._do_primary_checks():
            return

        slot_nos = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and \
                pslot.car.colour == colour:
                slot_nos += '%s ' % pslot.slot_no

        if slot_nos:
            print ('{}'.format(slot_nos[:-1]))
        else:
            print ("Not found")

    def slot_number_for_registration_number(self, reg_no):

        if not self._do_primary_checks():
            return

        slot_no = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and \
                pslot.car.reg_no == reg_no:
                slot_no = pslot.slot_no
                break

        if slot_no:
            print ('{}'.format(slot_no))
        else:
            print ("Not found")
