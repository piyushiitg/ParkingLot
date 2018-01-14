import lot, car

class Parking(object):
    """
    Parking class which has details about parking slots
    as well as operation performed on parking are present here
    """

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, no_of_slots):
        """This method will create parking lot if not present already with given
        number of slots.
        Input: no_of_slots - Integer Type
        """
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print "Parking Lot already created"
            return

        if no_of_slots > 0:
            for i in range(1, no_of_slots+1):
                temp_slot = lot.PSlot(slot_no=i,
                                    available=True)
                self.slots[i] = temp_slot
            print "Created a parking lot with %s slots" % no_of_slots
        else:
            print "Number of slots provided is incorrect."
        return

    def get_nearest_available_slot(self):
        """Method to find nearest available slot in parking
        """
        available_slots = filter(lambda x: x.available, self.slots.values())
        if not available_slots:
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]

    def park(self, reg_no, colour):
        """Method to park a coming car in nearest available parking
        slot. If not present it will throw message.
        Input: reg_no - String Type
               colour - String Type
        """

        if not self._do_primary_checks():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            # create car object and save in the available slot
            available_slot.car = car.Car.create(reg_no, colour)
            available_slot.available = False
            print "Allocated slot number: %s" % available_slot.slot_no
        else:
            print "Sorry, parking lot is full."

    def leave(self, slot_no):
        """Method to empty a parking slot while car is leaving.
        Input: slot_no - Integer Type
        """
        slot_no = int(slot_no)
        if not self._do_primary_checks():
            return

        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car:
                pslot.car = None
                pslot.available = True
                print "Slot number %s is free" % slot_no
            else:
                print "No car is present at slot number %s" % slot_no
        else:
            print "Sorry, slot number does not exist in parking lot."

    def status(self):
        """Method to show current status of parking
        """

        if not self._do_primary_checks():
            return

        print "Slot No\tRegistration No\tColour"
        for i in self.slots.values():
            if not i.available and i.car:
                print "%s\t%s\t%s" % (i.slot_no, i.car.reg_no, i.car.colour)

    def _do_primary_checks(self):
        if len(self.slots) == 0:
            print "Parking Lot not created"
            return False
        return True

    def registration_numbers_for_cars_with_colour(self, colour):
        """Method to find registration numbers of car with given colour in
        parking
        Input: colour - String Type
        """

        if not self._do_primary_checks():
            return

        reg_nos = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and \
                pslot.car.colour == colour:
                reg_nos += '%s ' % pslot.car.reg_no

        if reg_nos:
            print reg_nos[:-1]
        else:
            print "Not found"

    def slot_numbers_for_cars_with_colour(self, colour):
        """Method to find slot numbers for cars with given colour in
        parking.
        Input: colour - String Type
        """

        if not self._do_primary_checks():
            return

        slot_nos = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and \
                pslot.car.colour == colour:
                slot_nos += '%s ' % pslot.slot_no

        if slot_nos:
            print slot_nos[:-1]
        else:
            print "Not found"

    def slot_number_for_registration_number(self, reg_no):
        """Method to find slot numbers in parking with given registration
        number.
        Input: reg_no - String Type
        """

        if not self._do_primary_checks():
            return

        slot_no = ''
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and \
                pslot.car.reg_no == reg_no:
                slot_no = pslot.slot_no
                break

        if slot_no:
            print slot_no
        else:
            print "Not found"

