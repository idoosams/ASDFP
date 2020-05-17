
class Parser():
    def parse_snapshot(self, snapshot, config_fields):
        for field in snapshot.DESCRIPTOR.fields:
            if field.name not in config_fields:
                snapshot.ClearField(field.name)
        return snapshot
