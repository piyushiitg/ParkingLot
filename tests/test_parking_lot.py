import unittest
import env
from src import parking

class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = parking.Parking()
        cls.allocated_slot = 1

    def test_a_create_parking_lot(self):
        parking_slots = 6
        self.parking.create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking.slots), parking_slots, msg="Wrong parking lot created")

    def test_b_park(self):
        reg_no = "MH-12-FF-2017"
        colour = "Black"
        self.parking.park(reg_no, colour)
        self.assertFalse(self.parking.slots[self.allocated_slot].available, "Park failed.")
        for i in self.parking.slots.values():
            if not i.available and i.car:
                self.assertEqual(i.car.reg_no, reg_no, "Park failed")
                self.assertEqual(i.car.colour, colour, "Park failed")

    def test_c_leave(self):
        self.parking.leave(self.allocated_slot)
        self.assertTrue(self.parking.slots[self.allocated_slot].available, "Leave failed.")

    @classmethod
    def tearDownClass(cls):
        del cls.parking

if __name__ == '__main__':
    unittest.main()

