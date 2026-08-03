                +----------------+
                |     CLI        |
                +-------+--------+
                        |
                        v
              +-------------------+
              | ingestion layer   |
              +-------------------+
                /             \
               /               \
              v                 v
        CSV connector     Greenhouse connector
              \               /
               \             /
                v           v
              JobPosting objects
                     |
                     v
              existing pipeline
      parser → storage → matcher → ranker → reports