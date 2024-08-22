sysfs = '/sys/class/power_supply/BAT0/'

info_files = (
    'manufacturer',
    'model_name',
    'present',
    'technology',
    'type',

    'alarm',
    'capacity',
    'capacity_level',
    'charge_control_end_threshold',
    'cycle_count',
    'energy_full',
    'energy_full_design',
    'energy_now',
    'power_now',
    'status',
    'voltage_min_design',
    'voltage_now',
    # 'serial_number',
    # 'uevent',
)


def get_time(hours):
    hour = int(hours)
    minute = (hours % 1) * 60
    return f'{hour}h {minute:.0f}m'


battery_info = {}

for file in info_files:
    content = open(sysfs + file, 'r').read().strip()
    battery_info[file] = content

power = int(battery_info['power_now'])
energy = int(battery_info['energy_now'])
full = int(battery_info['energy_full'])
threshold = int(battery_info['charge_control_end_threshold']) / 100

if power == 0:
    time_display = ''
elif battery_info['status'].lower() == 'charging':
    time = (full * threshold - energy) / power
    time_display = f'Time to charge:    {get_time(time)} (to {threshold:.0%})'
elif battery_info['status'].lower() == 'discharging':
    time = energy / power
    time_display = f'Time to discharge: {get_time(time)}'


print(f'Battery Info ({sysfs}):')

print(f'''
Manufacturer: {battery_info['manufacturer']}
Model name:   {battery_info['model_name']}
Type:         {battery_info['type']}
Technology:   {battery_info['technology']}
Present:      {bool(battery_info['present'])}

Capacity:          {battery_info['capacity']}% ({battery_info['capacity_level']})
Charge threshold:  {battery_info['charge_control_end_threshold']}%
Cycle count:       {battery_info['cycle_count']}
Energy now:        {int(battery_info['energy_now']) / 1000000}Wh
Energy full:       {int(battery_info['energy_full']) / 1000000}Wh ({int(battery_info['energy_full']) / int(battery_info['energy_full_design']):.0%} design)
E. full design:    {int(battery_info['energy_full_design']) / 1000000}Wh
Power now:         {int(battery_info['power_now']) / 1000000}W
Alarm:             {int(battery_info['alarm']) / 1000000}J ({int(battery_info['alarm']) / int(battery_info['energy_full']):.0%})
Status:            {battery_info['status']}
{time_display}

Voltage now:        {int(battery_info['voltage_now']) / 1000000}V
Voltage_min design: {int(battery_info['voltage_min_design']) / 1000000}V
''')

input('Press Enter to exit...')