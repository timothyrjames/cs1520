class User(object):
  """Represents a user of this application."""
  def __init__(self, userid, username):
    self.userid = userid
    self.username = username
    self.credentials = {}

  def add_credential(self, credid):
    self.credentials[credid] = True

  def remove_credential(self, credid):
    self.credentials[credid] = False

  def to_dict(self):
    return {
      'id': self.userid,
      'username': self.username,
    }


class Credential(object):
  """Represents a credential for a user."""
  def __init__(self, credid, name):
    self.name = name
    self.credid = credid
    self.prereqs = []

  def add_prereq(self, prereq):
    self.prereqs.append(prereq)
  
  def to_dict(self):
    result = {
      'name': self.name,
      'credid': self.credid,
      'prereqs': []
    }
    for prereq in self.prereqs:
      result.prereqs.append(prereq.to_dict())
    return result