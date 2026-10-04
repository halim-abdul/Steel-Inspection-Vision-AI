from src.sensors.window import RollingWindow

def test_window():
    w=RollingWindow(2); w.push(1); assert not w.ready(); w.push(2); assert w.ready(); assert w.values()==[1.0,2.0]
