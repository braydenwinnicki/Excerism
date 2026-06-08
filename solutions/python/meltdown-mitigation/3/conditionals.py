"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""

    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""

    generated_power = voltage * current
    level = (generated_power/theoretical_max_power)*100

    if level >= 80: 
        return "green"
    elif level >= 60:
        return "orange"
    elif level >= 30:
        return "red"
    return "black"
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""

    current = temperature * neutrons_produced_per_second

    if current < .90 * threshold:
        return "LOW"
    if .90 * threshold <= current <= 1.10 * threshold:
        return "NORMAL"
    return  "DANGER"
