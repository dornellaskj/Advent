import requests
import json
import re

packages = []
with open("safe_data.txt", "r") as file:
    packages = [line.strip() for line in file]

def fetch_package_lock(github_url):
    """
    Fetch package-lock.json from GitHub URL
    Expected URL format: https://github.com/user/repo/blob/branch/package-lock.json
    """
    # Convert GitHub blob URL to raw URL
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        return json.loads(response.text)
    except requests.RequestException as e:
        print(f"Error fetching package-lock.json: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def extract_packages_from_lock(package_lock_data):
    """
    Extract package names from package-lock.json
    """
    packages_found = set()
    
    if "dependencies" in package_lock_data:
        packages_found.update(package_lock_data["dependencies"].keys())
    
    if "packages" in package_lock_data:
        for package_path, package_info in package_lock_data["packages"].items():
            if package_path and package_path != "":
                # Remove node_modules/ prefix if present
                package_name = package_path.replace("node_modules/", "")
                if package_name:
                    packages_found.add(package_name)
    
    return packages_found

def scan_packages_against_safe_list(lock_packages, safe_packages):
    """
    Compare packages from lock file against safe packages list
    """
    safe_set = set(safe_packages)
    lock_set = set(lock_packages)
    
    unsafe_packages = lock_set - safe_set
    safe_packages_found = lock_set & safe_set
    
    return {
        'total_packages': len(lock_set),
        'safe_packages': list(safe_packages_found),
        'unsafe_packages': list(unsafe_packages),
        'safe_count': len(safe_packages_found),
        'unsafe_count': len(unsafe_packages)
    }

# Main scanning function
def scan_github_package_lock(github_url):
    """
    Main function to scan a GitHub package-lock.json against safe packages
    """
    print(f"Fetching package-lock.json from: {github_url}")
    
    # Fetch the package-lock.json
    lock_data = fetch_package_lock(github_url)
    if not lock_data:
        return
    
    # Extract packages
    lock_packages = extract_packages_from_lock(lock_data)
    print(f"Found {len(lock_packages)} packages in lock file")
    
    # Scan against safe list
    results = scan_packages_against_safe_list(lock_packages, packages)
    
    # Display results
    print(f"\n--- Scan Results ---")
    print(f"Total packages: {results['total_packages']}")
    print(f"Safe packages: {results['safe_count']}")
    print(f"Unsafe packages: {results['unsafe_count']}")
    
    if results['unsafe_packages']:
        print(f"\n--- Unsafe Packages ---")
        for pkg in sorted(results['unsafe_packages']):
            print(f"  ⚠️  {pkg}")
    
    if results['safe_packages']:
        print(f"\n--- Safe Packages (first 10) ---")
        for pkg in sorted(results['safe_packages'])[:10]:
            print(f"  ✅ {pkg}")
        if len(results['safe_packages']) > 10:
            print(f"  ... and {len(results['safe_packages']) - 10} more")
    
    return results


github_url = "https://github.com/ElasticSuite/scramble-com/blob/master/yarn.lock"
scan_github_package_lock(github_url)
