def check_binary_search_tree_(root,valmin=0,valmax=1e4):
  if root is None:
    return True
  elif root.data>valmin and root.data<valmax:
    return check_binary_search_tree_(root.left,valmin,root.data) and check_binary_search_tree_(root.right,root.data,valmax)
  else:
    return False
