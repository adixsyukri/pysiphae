def groupfinder(identity, request):
    result = []
    if 'repoze.who.userid' in identity:
        id_ = identity['repoze.who.userid']
        result.append('group:LoggedIn')
        result.append('group:%s' % id_)
    if 'memberOf' in identity:
        # ldap memberOf
        for group in identity['memberOf']:
            groupname = group.split(',')[0].split('=')[1]
            result.append('group:%s' % groupname)
    # append from settings override
    settings = request.registry.settings
    if 'pysiphae.roles' in settings:
        entries = settings['pysiphae.roles'].strip().split('\n')
        for entry in entries:
            entry = entry.strip()
            if not entry: continue
            u,g = entry.split('=')
            if u == identity['repoze.who.userid']:
                result += g.split(',')
    return result