"""Symmetric 두 이진트리가 대칭 확인, 거울에 비친 듯 같은지 확인하는"""
def Symmetric(root1, root2):
    if not root1 and not root2: #둘 다 비어있ㅇ면 같은것 true
        return True
    
    if not root1 or not root2 or root1.val != root2.val:
        #한쪽만 비거나, 값이 다르면 짝이 안맞다. false
        return False
    
    return Symmetric(root1.left,root2.right) and Symmetric(root1.right, root2.left)
# 왼쪽-오른쪽, 오른쪽-왼쪽 이 서로 대칭인지 확인



"""Balance 두 이진트리가 균형인지 확인, 왼쪽과 오른쪽의 키 차이가 1보다 크면 안된다는 규칙 검사"""
def checkHeight(node):
    if not node: return 0 #노드가 비어있으면 height는 0
    
    left_h = checkHeight(node.left)
    right_h = checkHeight(node.right)
    
    if left_h == -1 or right_h == -1 : return -1
    #불균형 -1 이 발견된다면 불합격 -1 반환
    
    if abs(left_h - right_h) > 1: return -1
    #키차이가 1보다 크면 불합격 -1로 반환
    
    return max(left_h, right_h) + 1
    #정상이면 더 큰쪽 높이에 1을 더해 보고??
    
def Balanced(root):
    return checkHeight(root) != -1


"""유효한 바이너리 서치 트리 BST 인지 확인, 모든 왼쪽은 나보다 작고, 모든 오른쪽은 나보다 큰지 검사"""
def validBST(node, min_val=float('-inf'), max_val=float('inf')):
    #끝까지 에러없이 내려가면 true
    if not node: return True
    
    #현재 노드의 값이 정해진 범위(min~max)를 벗어나면 false
    if not (min_val < node.val < max_val)
        return False

    #왼쪽으로 갈 땐 최대값을 나로 제한, 오른쪽으로갈 땐 최소값을 나로 제한
    return (validBST(node.left, min_val, node.val) and 
            validBST(node.right, node.val, max_val))  
    #왼쪽으로 갈때 최소값min_val은 그대로 지키되, 최대값은 나node.val보다작아야해, 
    #오른쪽으로 갈때 최대값max_val은 그대로 유지하되, 최소값은 나node.val보다는 커야해
    #왼쪽으로도 오른쪽으로도 합격이어야 전체가 합격
    
"""노드마다 고유한 허용범위를 부여하고, 아래로 내려갈수록 그범위를 깍아감
모든 노드를 딱 한번씩만 검사하므로 시간복잡도 O(N)"""

