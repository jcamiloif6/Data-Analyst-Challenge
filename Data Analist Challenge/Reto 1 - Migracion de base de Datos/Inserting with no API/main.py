import subprocess

# Creating database
print("Creating challenges database...")
print("")

# Exec challenges.py - Creating table Challenges Details
print("Creating challenges table...")
subprocess.run(['python', 'challenges.py'])
print("Table Challenges Details created succesfully!")
print("")

# Exec profiles.py - Creating table profiles
print("Creating profiles table...")
subprocess.run(['python', 'profiles.py'])
print("Table profiles created succesfully!")
print("")

# Exec users.py - Creating table users
print("Creating users table...")
subprocess.run(['python', 'users.py'])
print("Table users created succesfully!")
print("")

# Exec resumes.py - Creating table resumes
print("Creating resumes table...")
subprocess.run(['python', 'resumes.py'])
print("Table resumes created succesfully!")
print("")

print("Migration completed.")
