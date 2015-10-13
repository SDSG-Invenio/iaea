
# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Zenodo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.


# def descriptor_autocomplete(dummy_form, dummy_field, term, limit=50):
#     from invenio.modules.communities.models import Community

#     if not term:
#         objs = Community.query.limit(limit).all()
#     else:
#         term = '%' + term + '%'
#         objs = Community.query.filter(
#             Community.title.like(term) | Community.id.like(term),
#             Community.id != 'zenodo'
#         ).filter_by().limit(limit).all()

#     return map(
#         lambda o: {
#             'value': o.title,
#             'fields': {
#                 'identifier': o.id,
#                 'title': o.title,
#                 'curatedby': o.owner.nickname,
#                 'description': o.description,
#                 'provisional': True,
#             }
#         },
#         objs
#     )

identifiers = ['CHEMISTRY', 'COMPUTERS', 'EDUCATION',
               'INFORMATION RETRIEVAL', 'ON-LINE SYSTEMS',
               'RESEARCH PROGRAMS', 'TECHNOLOGY TRANSFER']


def descriptor_autocomplete(dummy_form, dummy_field, term, limit=50):
    term = term.upper()
    r = []
    for i in identifiers:
        if term in i:
            d = {}
            d['value'] = i
            d['fields'] = {'identifier': i}
            r.append(d)
    return r
