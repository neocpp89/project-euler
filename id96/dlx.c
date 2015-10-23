#include <stdlib.h>
#include <stdio.h>
#include "dlx.h"

const int kHeaderColumnRow = -1;

void dlx_insert_rightof(struct dlx_node *to_insert, struct dlx_node *left)
{
    if (to_insert == NULL) {
        return;
    }
    if (left == NULL) {
        return;
    }

    struct dlx_node *right = left->right;
    if (right == NULL) {
        return;
    }
    right->left = to_insert;
    left->right = to_insert;
    to_insert->left = left;
    to_insert->right = right;
    return;
}

void dlx_insert_upof(struct dlx_node *to_insert, struct dlx_node *down)
{
    if (to_insert == NULL) {
        return;
    }
    if (down == NULL) {
        return;
    }

    struct dlx_node *up = down->up;
    if (up == NULL) {
        return;
    }
    up->down = to_insert;
    down->up = to_insert;
    to_insert->down = down;
    to_insert->up = up;
    return;
}

void dlx_cover_horizontal(struct dlx_node *node)
{
    if (node == NULL) {
        return;
    }
    struct dlx_node *left = node->left;
    struct dlx_node *right = node->right;
    if (left == NULL || right == NULL) {
        return;
    }

    left->right = right;
    right->left = left;
    return;
}

void dlx_cover_vertical(struct dlx_node *node)
{
    if (node == NULL) {
        return;
    }
    struct dlx_node *up = node->up;
    struct dlx_node *down = node->down;
    if (up == NULL || down == NULL) {
        return;
    }

    up->down = down;
    down->up = up;
    return;
}

void dlx_uncover_horizontal(struct dlx_node *node)
{
    if (node == NULL) {
        return;
    }
    struct dlx_node *left = node->left;
    struct dlx_node *right = node->right;
    if (left == NULL || right == NULL) {
        return;
    }

    left->right = node;
    right->left = node;
    return;
}

void dlx_uncover_vertical(struct dlx_node *node)
{
    if (node == NULL) {
        return;
    }
    struct dlx_node *up = node->up;
    struct dlx_node *down = node->down;
    if (up == NULL || down == NULL) {
        return;
    }

    up->down = node;
    down->up = node;
    return;
}

void dlx_cover_column(struct dlx_node *colheader)
{
    dlx_cover_horizontal(colheader);

    for (struct dlx_node *colnode = colheader->up; colnode != colheader; colnode = colnode->up) {
        for (struct dlx_node *rownode = colnode->right; rownode != colnode; rownode = rownode->right) {
            dlx_cover_vertical(rownode);
            rownode->column_header->num_elements--;
        }
    }
    return;
}

void dlx_uncover_column(struct dlx_node *colheader)
{
    for (struct dlx_node *colnode = colheader->down; colnode != colheader; colnode = colnode->down) {
        for (struct dlx_node *rownode = colnode->left; rownode != colnode; rownode = rownode->left) {
            dlx_uncover_vertical(rownode);
            rownode->column_header->num_elements++;
        }
    }

    dlx_uncover_horizontal(colheader);
    return;
}

struct dlx_node *dlx_insert_column(struct dlx_matrix *m, int col)
{
    struct dlx_node *insert = NULL;
    for (struct dlx_node *colheader = m->head->right; colheader != m->head; colheader = colheader->right) {
        if (colheader->col == col) {
            insert = colheader;
            break;
        }
    }

    if (insert == NULL) {
        insert = malloc(sizeof(struct dlx_node));
        insert->up = insert;
        insert->down = insert;
        insert->col = col;
        insert->row = kHeaderColumnRow;
        insert->num_elements = 0;
        insert->is_optional = 0;
        insert->column_header = NULL;
        dlx_insert_rightof(insert, m->head);
    }

    return insert;
}

void dlx_matrix_insert(struct dlx_matrix *m, int row, int col)
{
    struct dlx_node *colheader = dlx_insert_column(m, col);
    for (struct dlx_node *colnode = colheader->up; colnode != colheader; colnode = colnode->up) {
        if (colnode->row == row) {
            return;
        }
    }

    struct dlx_node *to_insert = malloc(sizeof(struct dlx_node));
    if (to_insert == NULL) {
        return;
    }
    to_insert->column_header = colheader;
    to_insert->left = to_insert;
    to_insert->right = to_insert;
    to_insert->row = row;
    to_insert->col = col;
    dlx_insert_upof(to_insert, colheader);
    colheader->num_elements++;

    for (struct dlx_node *othercolheader = m->head->right; othercolheader != m->head; othercolheader = othercolheader->right) {
        if (othercolheader == colheader) {
            continue;
        }
        for (struct dlx_node *othercolnode = othercolheader->up; othercolnode != othercolheader; othercolnode = othercolnode->up) {
            if (othercolnode->row == row) {
                dlx_insert_rightof(to_insert, othercolnode);
                return;
            }
        }
    }

    return;
}

void dlx_search(struct dlx_matrix *m, int depth, int *selected)
{
    int num_primary_columns = 0;

    struct dlx_node *most_constrained_colheader = NULL;
    for (struct dlx_node *colheader = m->head->right; colheader != m->head; colheader = colheader->right) {
        if (colheader->is_optional == 1) {
            continue;
        }

        if (most_constrained_colheader == NULL) {
            most_constrained_colheader = colheader;
        } else if (most_constrained_colheader->num_elements > colheader->num_elements) {
            most_constrained_colheader = colheader;
        }
        num_primary_columns++;
    }

    // success
    if ((num_primary_columns == 0) || (most_constrained_colheader == NULL)) {
        if (depth == 81) {
            int g[81];
            for (int k = 0; k < depth; k++) {
                // printf("%d ", selected[i]);
                int s = selected[k];
                int i = (s / 81) % 9;
                int j = (s / 9) % 9;
                int n = (s % 9) + 1;
                g[9*i + j] = n;
            }
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    // printf("%d ", g[i*9 + j]);
                }
                // printf("\n");
            }
            // printf("Valid.\n");
            printf("%d%d%d\n", g[0], g[1], g[2]);
        }
        /*
        for (int i = 0; i < depth; i++) {
            printf("%d ", selected[i]);
        }
        */
        printf("\n");
        return;
    }

    if (most_constrained_colheader->num_elements == 0) {
        // failure, get out;
        return;
    }

    dlx_cover_column(most_constrained_colheader);

    for (struct dlx_node *colnode = most_constrained_colheader->up; colnode != most_constrained_colheader; colnode = colnode->up) {
        selected[depth] = colnode->row;

        for (struct dlx_node *rownode = colnode->right; rownode != colnode; rownode = rownode->right) {
            dlx_cover_column(rownode->column_header);
        }
        dlx_search(m, depth + 1, selected);
        for (struct dlx_node *rownode = colnode->left; rownode != colnode; rownode = rownode->left) {
            dlx_uncover_column(rownode->column_header);
        }
    }

    dlx_uncover_column(most_constrained_colheader);

    return;
}

void dlx_set_optional(struct dlx_matrix *m, int col)
{
    for (struct dlx_node *colheader = m->head->right; colheader != m->head; colheader = colheader->right) {
        if (colheader->col == col) {
            colheader->is_optional = 1;
            break;
        }
    }
    return;
}

void dlx_set_required(struct dlx_matrix *m, int col)
{
    for (struct dlx_node *colheader = m->head->right; colheader != m->head; colheader = colheader->right) {
        if (colheader->col == col) {
            colheader->is_optional = 0;
            break;
        }
    }
    return;
}

struct dlx_matrix *dlx_matrix_create()
{
    struct dlx_matrix *m = malloc(sizeof(struct dlx_matrix));
    if (m != NULL) {
        m->head = malloc(sizeof(struct dlx_node));
        if (m->head != NULL) {
            m->head->up = m->head;
            m->head->down = m->head;
            m->head->left = m->head;
            m->head->right = m->head;
            m->head->col = kHeaderColumnRow;
            m->head->row = kHeaderColumnRow;
        }
    }
    return m;
}

void dlx_matrix_delete(struct dlx_matrix *m)
{
    if (m != NULL) {
        if (m->head != NULL) {
            for (struct dlx_node *colheader = m->head->right; colheader != m->head; ) {
                struct dlx_node *right = colheader->right;
                for (struct dlx_node *colnode = colheader->up; colnode != colheader; ) {
                    struct dlx_node *up = colnode->up;
                    free(colnode);
                    colnode = up;
                }
                free(colheader);
                colheader = right;
            }
            free(m->head);
        }
        free(m);
    }
    return;
}
