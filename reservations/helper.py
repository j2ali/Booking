from datetime import datetime, timedelta


def get_available_time_slots(hours, appointments, duration=timedelta(hours=1)):
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    available_time_slots = []
    for start, end in ((slots[i][1], slots[i + 1][0]) for i in range(len(slots) - 1)):
        assert start <= end, "Cannot attend all appointments"
        while start + duration <= end:
            available_time_slots.append("{:%H:%M} - {:%H:%M}".format(start, start + duration))
            start += duration
    return available_time_slots


def build_appointments_list(appointments):
    appointments_list = []
    for appointment in appointments:
        appointments_list.append(appointment.time_slot)
    return appointments_list