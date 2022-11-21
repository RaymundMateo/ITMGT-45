def material_waste(total_material, material_units, num_jobs, job_consumption):
    return (f'{((num_jobs * job_consumption) - total_material)}' + material_units)

print(material_waste(10, "kg", 15, 8))