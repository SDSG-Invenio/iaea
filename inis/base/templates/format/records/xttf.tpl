{% for recid in recids -%}
  {{ format_record(recid, of=of) | safe}}
{%- endfor %}