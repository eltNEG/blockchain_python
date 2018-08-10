from leveldb import LevelDB, WriteBatch


class Lvldb():
    def __init__(self, filename, **kwargs):
        self.Level = LevelDB(filename, **kwargs)

    def put(self, key, value, sync=False):
        key = key.encode()
        value = value.encode()
        self.Level.Put(key, value, sync)

    def get(self, key, verify_checksums=False, fill_cache=True):
        key = key.encode()
        return (self.Level.Get(key, verify_checksums, fill_cache)).decode()

    def save_get(self, key, verify_checksums=False, fill_cache=True):
        try:
            res = self.get(key, verify_checksums=False, fill_cache=True)
            return res        
        except KeyError:
            return None

    def delete(self, key, sync=False):
        return self.Level.Delete(key, sync=False)

    def write(self, batch, sync=True):
        return self.Level.Write(batch, sync)

"""
    def get_stats(self):
        return self.Level.GetStats()
"""
class Lvlbatch():
    def __init__(self):
        self.Batch = WriteBatch()

    def put(self, key, value):
        key = key.encode()
        value = value.encode()
        return self.Batch.Put(key, value)

    def delete(self, key):
        key = key.encode()
        return self.Batch.Delete(key)
