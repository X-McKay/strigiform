"""Queries for webapp."""

observation_query = """
                        select t.*, o.date
                        from taxonomy t
                        left join observations o
                        on o.taxon_order = t.taxon_order
                    """
