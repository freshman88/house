
def save_file(name, content):
    with open(name, 'wb') as f:
        f.write(content)
        f.close()

if __name__ == "__main__":
    # test
    save_file('tmp/x0.html', b"aabb")
