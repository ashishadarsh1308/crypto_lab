from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Generate a new DSA private key
def generate_key():
    private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    return private_key

# Sign a message
def sign_message(private_key, message):
    signature = private_key.sign(message, hashes.SHA256())
    return signature

# Verify a signature
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message, hashes.SHA256())
        return True
    except Exception:
        return False

# Serialize the keys to save them
def serialize_keys(private_key, public_key):
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()  # No encryption
    )
    
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_bytes, public_bytes

# Main function
def main():
    # Generate keys
    private_key = generate_key()
    public_key = private_key.public_key()

    # Serialize keys
    private_bytes, public_bytes = serialize_keys(private_key, public_key)
    
    # Save keys to files
    with open("private_key.pem", "wb") as f:
        f.write(private_bytes)

    with open("public_key.pem", "wb") as f:
        f.write(public_bytes)

    # Create a message
    message = b"Hello, this is a secret message!"

    # Sign the message
    signature = sign_message(private_key, message)
    print("Signature:", signature)

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print("Signature valid:", is_valid)

if __name__ == "__main__":
    main()
